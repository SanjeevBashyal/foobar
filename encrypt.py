import base64

# remove spaces
encrypted = "CEYdHwYGE10RRlNSWUYLQlQSFUlGRUIVQQ4NFgkeFAkXEUlBSQ8WERNLDwQXT1VBS1VXFQ4cHhZC VhRCRhoGGhMJVFgRDQtNSUVRTwEJGg0PBAFVXwdGTlBFQgNADg4QAxwFSxwRVBMPCAcMAl1FQUlI XhINVlRUTU5NAwoZCUJbU08OCAIRFg4="
decoded = base64.b64decode(encrypted)
key = 'sanjeev.bashyal01'
encoded = str.encode(key)

decrypted = ""
for i in range(len(decoded)):
    decrypted += chr((encoded[i%len(encoded)]^decoded[i]))

print(decrypted)