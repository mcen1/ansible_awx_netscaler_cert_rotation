: IT Ops team would like to build a process that will automate the renewal and subsequent installation of load balancer certificates onto the NetScaler. There is talk from Google that a new requirement of max of 90 expiry could be on the horizon will force us to complete this.

https://www.sectigo.com/resource-library/google-announces-intentions-to-limit-tls-certificates-to-90-days-why-automated-clm-is-crucial

This will require use of the Citrix NetScaler ADM Nitro API 
https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/ to find which certs are expiring.

and the Sectigo CertManager API 
https://www.sectigo.com/uploads/audio/Certificate-Manager-20.1-Rest-API.html to generate certificates

