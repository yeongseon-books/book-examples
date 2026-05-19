from common import TLSCertParser


def test_tls_parser_pem_markers():
    parsed = TLSCertParser().parse_pem_text(
        "-----BEGIN CERTIFICATE-----\nX\n-----END CERTIFICATE-----"
    )
    assert parsed["has_begin"] and parsed["has_end"]
