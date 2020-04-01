from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials


class KeyVault:
    client = None

    def login(self, credentials=None):
        if credentials is None:
            credentials = ServicePrincipalCredentials(
                client_id = '***********************',  #appId
                secret    = '***********************',     #password
                tenant    = '***********************'
            )
        self.client = KeyVaultClient(credentials)

    def getSecret(self, secret_info=None):
        vault_url = None
        secret_id = None
        secret_version = None

        if secret_info is None:
            vault_url = 'https://*****.vault.azure.net/'
            secret_id = '**********'
            secret_version = '*************'
        else:
            vault_url = secret_info.vault_uri
            secret_id = secret_info.secret_id
            secret_version = secret_info.secret_version

        secret_bundle = self.client.get_secret(vault_url, secret_id, secret_version)
        secret = secret_bundle.value

        return secret

if __name__ == "__main__":
    kv = KeyVault()
    kv.login()
    secret = kv.getSecret()
    print(secret)
