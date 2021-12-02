from Animals import Fox, Bird, Cat, Dog, Mouse, Cow, Frog, Elephant, Duck, Fish, Seal

def yelling_animals():
    fx = Fox()
    b = Bird()
    ct = Cat()
    dg = Dog()
    m = Mouse()
    cw = Cow()
    fg = Frog()
    e = Elephant()
    dk = Duck()
    fh = Fish()
    s = Seal()

    tpl = (fx, b, ct, dg, m, cw, fg, e, dk, fh, s)

    for i in tpl:
        i.say()


yelling_animals()
