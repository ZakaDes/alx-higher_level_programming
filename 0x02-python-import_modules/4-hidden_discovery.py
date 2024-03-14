#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    lng = len(n)
    for i in range(0, lng):
        if n[i][:2] != "__":
            print(n[i])
