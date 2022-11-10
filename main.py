
def main():
    filename = "level4/level4.txt"
    bid, instant_price, bids = parse(get_file(filename))
    print(bid)
    print(bids)

    history = f'-,{bid}'

    highest_bid = bids[0][1]
    highest_bidder = bids[0][0]
    bids.pop(0)

    history += f',{highest_bidder},{bid}'

    for i in bids:
        if instant_price != 0:
            if highest_bid >= instant_price:
                if i[0] == highest_bidder:
                    continue
                history += f',{highest_bidder},{instant_price}'
                continue
            elif i[1] >= instant_price:
                history += f',{i[0]},{highest_bid+1}'
                highest_bidder = i[0]
                highest_bid = i[1]
                continue

        if i[0] == highest_bidder:
            if i[1] > highest_bid:
                highest_bid = i[1]
        elif i[1] >= bid:
            bid = i[1] + 1

            if i[1] > highest_bid:
                bid = highest_bid + 1
                highest_bidder = i[0]
                highest_bid = i[1]
            elif i[1] == highest_bid:
                bid = highest_bid

            history += f',{highest_bidder},{bid}'

    print(f'{history}')


def parse(input: [str]) -> (int, []):
    print("parsing...")
    string_bid = int(input.pop(0))
    instant_price = int(input.pop(0))
    bids = []

    while len(input) > 0:
        bids.append([input.pop(0), int(input.pop(0))])

    return string_bid, instant_price, bids


def get_file(filename: str):
    f = open(filename, "r")
    s = f.read()
    inputs = s.split(",")
    return inputs


if __name__ == '__main__':
    print("wir sind hardcore krass - gg ez")
    #main()
