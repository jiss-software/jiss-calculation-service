from tornado.options import define
from handler import HealthCheckHandler
from handler import CalculateOrderHandler

define("port", default=33004, help="Application port")
define("max_buffer_size", default=50 * 1024**2, help="")
define("autoreload", default=False, help="Autoreload server on change")

define("log_dir", default="log", help="Logger directory")
define("log_file", default="jiss-calculation-service.log", help="Logger file name")


routing = [
    (r"/", HealthCheckHandler),
    (r"/calculate/order", CalculateOrderHandler),
]
