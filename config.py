from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

# FASTAPI SETTINGS
APP_HOST = env.str("APP_HOST", "0.0.0.0")
APP_PORT = env.int("APP_PORT", 8000)

# KAFKA SETTINGS
CLIENT_ID = env.str("CLIENT_ID")
BOOTSTRAP_SERVERS = env.list("BOOTSTRAP_SERVERS")
KAFKA_ADDRESS_RESOLVE_TOPIC=env.str("KAFKA_ADDRESS_RESOLVE_TOPIC")
KAFKA_PROCESSED_TOPIC=env.str("KAFKA_PROCESSED_TOPIC")
HF_HUB_TOKEN = env.str("HF_HUB_TOKEN")
# GROUP_ID=env.int("GROUP_ID", None)

# Max message pool count
MAX_POOL_RECORDS=env.int("MAX_POOL_RECORDS")
MESSAGE_TIMEOUT_MS=env.int("MESSAGE_TIMEOUT_MS")
ENABLE_AUTO_COMMIT=env.bool("ENABLE_AUTO_COMMIT")

# Third party api key
GOOGLE_API_KEY = env.str("GOOGLE_API_KEY")
OPENAI_API_KEY = env.str("OPENAI_API_KEY")
NER_API_KEY = env.str("NER_API_KEY")
