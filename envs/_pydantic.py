from pydantic import BaseSettings


# ----------------------------- 1° Way -----------------------------
class SettingsModel(BaseSettings):
    DB_HOST: str

    class Config:
        # env_file = 'env.env'
        env_file = './envs/.env.dev'
        env_file_encoding = 'utf-8'


ENV = SettingsModel()
print(ENV)


# ----------------------------- 2° Way -----------------------------
class SettingsModel2(BaseSettings):
    DB_HOST: str


settings = SettingsModel2(_env_file='env.env', _env_file_encoding='utf-8')
print(settings)
