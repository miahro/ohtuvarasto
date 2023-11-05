from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto {olutta}")
    print(
        f"Olut getterit:\nsaldo = {olutta.saldo}\ntilavuus = {olutta.tilavuus}"
        f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}"
        f"\nMehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)

    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}"
          f"\nVirhetilanteita:\nVarasto(-100.0);\n{Varasto(-100.0)}"
          f"\nVarasto(100.0, -50.7)\n{Varasto(100.0, -50.7)}")

    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}"
          f"\nMehuvarasto: {mehua}\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}"
          f"\nOlutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    print(f"saatiin {olutta.ota_varastosta(1000.0)}\nOlutvarasto: {olutta}"
          f"\nMehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)"
          f"\nsaatiin {mehua.ota_varastosta(-32.9)}\nMehuvarasto: {mehua}")

    print("extra row that breaks pylint")


if __name__ == "__main__":
    main()
