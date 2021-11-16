import hashlib

key = "yzbqklnj"


def santa_md5(input):
    count = 1

    while True:
        running_key = key + str(count)
        result = hashlib.md5(running_key.encode('utf-8')).hexdigest()

        if result[:len(input)] == input:
            break

        count += 1

    return result, running_key, count


if __name__ == "__main__":
    print("Santa is mining AdventCoins...\n")

    result = santa_md5("00000")
    print("Hash: " + result[0] + "\nKey: " +
          result[1] + "\nAnswer: " + str(result[2]) + "\n")

    result = santa_md5("000000")
    print("Hash: " + result[0] + "\nKey: " +
          result[1] + "\nAnswer: " + str(result[2]))
