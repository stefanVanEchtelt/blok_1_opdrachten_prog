def kwadraten_som(grondgetallen):
    print(sum(map(lambda x : x**2, filter(lambda y: y >= 0, grondgetallen))))

kwadraten_som([4, 5, 3, -81])