from collections import Counter
class stats:
    def __init__(self):
        self.id_counter = Counter()

    def addID(self, id):
        self.id_counter[str(id)] += 1

    def printStats(self):
        print(f"{'Identifier':<30} {'Count':<10}")
        for id, count in sorted(self.id_counter.items(), key=lambda item:item[1], reverse=True):
            print(f"{id:<30} {count:<10}")

    def __str__(self):
        return str(self.id_counter)

    def __repr__(self):
        return f'IDs counter({str(self.id_counter)})'
