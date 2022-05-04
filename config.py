import configparser
import sys


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.dataset = self.config.read("config.ini")
        self.fixstrings = ["account_name", "prefix", "subprefix", "suffix"]

    def get(self, attribute, defaultvalue=""):
        data = ""

        if len(self.dataset) != 1:
            sys.tracebacklimit = 0
            sys.exit(
                "Cannot read config.ini! - Please make sure it exists in the folder where 3cqsbot.py is executed."
            )

        sections = self.config.sections()

        for section in sections:
            if self.config.has_option(section, attribute):
                raw_value = self.config[section].get(attribute)

                if raw_value:
                    if attribute in self.fixstrings:
                        data = raw_value
                    else:
                        data = self.check_type(raw_value)
                    break

        if data == "" and str(defaultvalue):
            data = defaultvalue
        elif data == "" and defaultvalue == "":
            sys.tracebacklimit = 0
            sys.exit(
                "Attribute "
                + attribute
                + " is not set, but mandatory! Please check the readme for configuration."
            )

        return data

    def isfloat(self, element):
        try:
            float(element)
            return True
        except ValueError:
            return False

    def check_type(self, raw_value):
        data = ""

        if raw_value.isdigit():
            data = int(raw_value)
        elif raw_value.lower() == "true":
            data = True
        elif raw_value.lower() == "false":
            data = False
        elif self.isfloat(raw_value):
            data = float(raw_value)
        else:
            data = str(raw_value)

        return data

[general]
debug = false
#log_to_file = false
#log_file_path = 3cqsbot.log
#log_file_size = 200000
#log_file_count = 5

[telegram]
api_id = 10167416
api_hash = 0 fe2b738ce309604930f0b1574b906fa
#sessionfile = tgsession
#chatroom = 3C Quick Stats

[commas]
key = 6 dd99172acf248a7aa59cd1d3530d51d267137b89b5e433daee4ac1b55803b42
secret = 1093ef3cb8c382a040b18b9e0ccf91267f040d9c2d5464a29e67119e123f625e90f91b0c969f6dbe91b93ab006f5a1031c8f8534e72526531400a862cd9400d7e785a2d00eb71c9927a6e84e0a4ea8a13a9589e8906d43783660ca700016d77d3aaf1051
#timeout = 3
#retries = 5
#delay_between_retries = 2.0
#system_bot_value = 300

[dcabot]
prefix = 3CQSBOT
subprefix = MULTI
suffix = TA_SAFE
tp = 1.5
bo = 11
so = 11
os = 1.05
ss = 1
sos = 2.4
mad = 1
max = 1
mstc = 25
sdsp = 1
single = false
single_count = 1
#btc_min_vol = 100
#cooldown = 30
#deals_count = 1

[trading]
market = USDT
trade_mode = paper
account_name = Paper Account 472699
#delete_single_bots = false
#singlebot_update = true
# Binance only
#trailing = false
#trailing_deviation = 0.2
# Futures trading only
trade_future = false
leverage_type = cross
leverage_value = 2
stop_loss_percent = 1
stop_loss_type = stop_loss_and_disable_bot
stop_loss_timeout_enabled = false
stop_loss_timeout_seconds = 5

[filter]
symrank_signal = triple100
#symrank_limit_min = 1
#symrank_limit_max = 100
#volatility_limit_min = 0.1
#volatility_limit_max = 100
#price_action_limit_min = 0.1
#price_action_limit_max = 100
# warning to not use this attribute for large bots!
# to not set it to 0
# topcoin_volume = 300
# not more then 3500
#topcoin_limit = 3500
#topcoin_exchange = binance
#limit_initial_pairs = false
#random_pair = true
# RSI-7 < 100 (means asap)
# single strategy
deal_mode = [{"options": {"time": "3m", "points": "100", "time_period": "7", "trigger_condition": "less"}, "strategy": "rsi"}]
# multiple strategies 
#deal_mode = [{"options": {"time": "5m", "type": "buy_or_strong_buy"}, "strategy": "trading_view"},{"options": {"time": "15m", "points": "70", "time_period": "7", "trigger_condition": "less"}, "strategy": "rsi"},{"options": {"time": "1h", "points": "70", "time_period": "7", "trigger_condition": "less"},{"options": {"time": "4h", "points": "70", "time_period": "7", "trigger_condition": "less"}]
#btc_pulse = false
# ATTENTION: if ext_botswitch set to true, btc_pulse will be ignored
#ext_botswitch = false
token_denylist = [USDT_BTC, USDT_ETH, USDT_BUSD, USDT_USDC]
