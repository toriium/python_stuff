from Crypto.PublicKey import RSA


def generate_rsa_par_keys():
    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')

    with open("private_key.pem", 'wb') as content_file:
        content_file.write(private_key)

    with open("public_key.pem", 'wb') as content_file:
        content_file.write(public_key)


if __name__ == '__main__':
    generate_rsa_par_keys()
