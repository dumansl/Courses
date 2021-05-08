def sesli_harf(cumle):
    sesliharf = "aeiıoöuüAEIİOÖUÜ"
    yeni = ""
    for i in cumle:
        if i not in sesliharf:
            yeni += i
    return yeni 

sesli_harf("Python problemi çözüyorum")

