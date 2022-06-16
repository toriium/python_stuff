from pydantic import BaseSettings


class SettingsModel(BaseSettings):
    DB_HOST: str

    class Config:
        # env_file = 'env.env'
        env_file = './envs/.env.dev'
        env_file_encoding = 'utf-8'


ENV = SettingsModel()
print(ENV)
