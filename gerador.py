import random as rd

nums = list(range(1, 61))

while True:
    j = abs(int(input(
        "\nQuantos jogos deseja gerar? "
    )))
    if j == 0:
        break
    n = abs(int(input(
        "\nQuantos números deseja gerar? "
    )))
    if n == 0:
        break
    print("\nJogos:")
    for i in range(j):
        jogo = [
            f"{x:02}"
            for x in rd.choices(nums, k=n)
        ]
        print(f"{(i + 1):>5}: {', '.join(jogo)}")
