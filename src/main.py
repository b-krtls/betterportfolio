# :FIXME: Module docstring and write the main function

from markets.cryptocurrency.fngindex import CryptoFearAndGreedIndex

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("info")  # DEBUG
logger.addHandler(logging.StreamHandler())

CryptoFearAndGreedIndex._test_me()