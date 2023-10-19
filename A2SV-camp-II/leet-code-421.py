class Solution:
    def __init__(self):
        self.root = {}

    def complement(self, number):
        bin_rep = bin(number)[2:]
        return int(''.join(['1' if bit == '0' else '0' for bit in bin_rep]), 2)

    def to_32_bit(self, number):
        return '{:032b}'.format(number)

    def insert(self, number):
        curr_node = self.root
        binary = self.to_32_bit(number)
        for bit in binary:
            if bit not in curr_node:
                curr_node[bit] = {}
            curr_node = curr_node[bit]
     
        curr_node['value'] = number

    def switch(self, bit):
        if bit == '0':
            return '1'
        return '0'

    def max_xor(self, list_numbers):
        curr_max = 0
        for number in list_numbers:
            target = self.to_32_bit(self.complement(number))
            curr_node = self.root
            for bit in target:
                if bit not in curr_node:
                    curr_node = curr_node[self.switch(bit)]
                else:
                    curr_node = curr_node[bit]
            curr_max = max(curr_node['value'] ^ number, curr_max)
        return curr_max

    def findMaximumXOR(self, nums: List[int]) -> int:
        for number in nums:
            self.insert(number)
        return self.max_xor(nums)
