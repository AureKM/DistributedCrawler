from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import FlatMapFunction
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors import FlinkKafkaConsumer

class FlinkURLProcessor:
    def __init__(self):
        self.env = StreamExecutionEnvironment.get_execution_environment()

    def deduplicate_urls(self, urls):
        """使用 Flink 进行 URL 去重"""
        # 将 URL 列表转换为数据流
        data_stream = self.env.from_collection(urls)

        # 去重逻辑
        unique_urls = data_stream \
            .map(lambda url: (url, 1)) \
            .key_by(lambda x: x[0]) \
            .reduce(lambda x, y: (x[0], x[1] + y[1])) \
            .filter(lambda x: x[1] == 1) \
            .map(lambda x: x[0])

        # 执行并获取结果
        result = unique_urls.execute_and_collect()
        return list(result)