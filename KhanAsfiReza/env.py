import os
import dotenv

dotenv.load_dotenv()
dotenv.load_dotenv(verbose=True)

# Django Secret Key
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# Database
DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE", "ENGINE")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "DBNAME")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "HOST")
DATABASE_USER = os.environ.get("DATABASE_USER", "USER")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "POST")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "PASSWORD")

# Production
PRODUCTION = int(os.environ.get("PRODUCTION", 0))
PRODUCTION_URL = os.environ.get("PRODUCTION_URL", "localhost")
