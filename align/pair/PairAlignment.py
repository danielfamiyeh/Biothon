class PairAlignment:
    def __init__(self, *args, **kwargs):
        """
        Pairwise alignment object constructor.
        :param args:    Two aligned strings and their alignment score
        :param kwargs:  s1_name, s2_name representing the names
                            given to the sequences durign construction
        """

        mismatches, no_gap = 0, 0

        # Assign sequence names
        self.s1_name = kwargs.get("s1_name", "")
        self.s2_name = kwargs.get("s2_name", "")

        # Assign sequence data
        self.seq1, self.seq2, self.score = args

        # Length of longest sequence name
        self.len_longest_name = max(len(self.s1_name), len(self.s2_name))

        # Iterate over both sequences
        for char1, char2 in zip(self.seq1, self.seq2):
            if char1 != "-" and char2 != "-":
                # Increment mismatch count
                mismatches += int(char1 != char2)
                # Increment not gapped count
                no_gap += 1

        # Calculate distance to 3 dp
        self.dist = round((mismatches/(no_gap if no_gap > 0 else 1) * 100), 3)

    def __str__(self):
        tab = '\t'
        # Print both sequences with tabs to align them
        return f"{self.s1_name}{' '*(self.len_longest_name-len(self.s1_name)) + tab*2}{self.seq1}\n"\
               + f"{' '*self.len_longest_name+2*tab}" + ''.join("|" if self.seq1[i] == self.seq2[i]\
               else " " for i in range(len(self.seq1))) + "\n" + \
               f"{self.s2_name}{' '*(self.len_longest_name-len(self.s2_name)) + tab*2}{self.seq2}\n"                \
               + "\n" + f"Score: {self.score}" + f"\nDistance: {self.dist}%"

    def __repr__(self):
        pass

    def __len__(self):
        return len(self.seq1)
