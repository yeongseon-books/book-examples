"""Information Security 101 - Episode 4: Tls and certificates."""

from common import TLSCertParser

pem = "-----BEGIN CERTIFICATE-----\nMIIB...\n-----END CERTIFICATE-----"
print(TLSCertParser().parse_pem_text(pem))
