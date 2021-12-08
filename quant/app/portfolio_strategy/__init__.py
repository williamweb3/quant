from pathlib import Path

from quant.trader.app import BaseApp
from quant.trader.constant import Direction
from quant.trader.object import TickData, BarData, TradeData, OrderData
from quant.trader.utility import BarGenerator, ArrayManager

from .base import APP_NAME
from .engine import StrategyEngine
from .template import StrategyTemplate
from .backtesting import BacktestingEngine


class PortfolioStrategyApp(BaseApp):
    """"""

    app_name = APP_NAME
    app_module = __module__
    app_path = Path(__file__).parent
    display_name = "组合策略"
    engine_class = StrategyEngine
    widget_name = "PortfolioStrategyManager"
    icon_name = "strategy.ico"
