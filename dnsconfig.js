// @ts-check
/// <reference path="types-dnscontrol.d.ts" />

var REG_NONE = NewRegistrar("none");    // No registrar.
var DNS_BIND = NewDnsProvider("bind");  // ISC BIND.

// Domains:

DEFAULTS(
    DefaultTTL("1m")
);

D("example.com", REG_NONE, DnsProvider(DNS_BIND),
    A("@", "192.168.0.1")
);
