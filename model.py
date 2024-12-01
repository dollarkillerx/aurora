class Model:
    direction = "sell"  # sell or buy
    magic = 666  # magic number
    currency_suffix = "m"  # currency suffix 货币后缀
    initial_volume = 0.01  # initial volume 初始数量
    increase_multiple = 1  # increase multiple 增量倍数
    interval = 60  # interval 加仓间隔
    time_interval = 20  # time interval 时间间隔 分
    stop_loss = 100  # stop loss 止损金额 美金

    def __init__(self, direction, magic, currency_suffix, initial_volume, increase_multiple, interval, time_interval,
                 stop_loss):
        self.direction = direction
        self.magic = magic
        self.currency_suffix = currency_suffix
        self.initial_volume = initial_volume
        self.increase_multiple = increase_multiple
        self.interval = interval
        self.time_interval = time_interval
        self.stop_loss = stop_loss
