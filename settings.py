from tornado.options import define
from handler import HealthCheckHandler

define("port", default=33001, help="Application port")
define("max_buffer_size", default=50 * 1024**2, help="")
define("autoreload", default=False, help="Autoreload server on change")

define("db_address", default="mongodb://localhost:27017", help="Database address")
define("db_name", default="test", help="Database name")

define("log_dir", default="log", help="Logger directory")
define("log_file", default="jiss-tornado-template.log", help="Logger file name")


routing = [
    (r"/", HealthCheckHandler),
]
