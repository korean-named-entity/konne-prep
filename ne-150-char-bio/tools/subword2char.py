"""

Usage:

subword2char.py valid raw_sent.txt subword_bio.txt > char_bio_valid.txt
subword2char.py conv raw_sent.txt subword_bio.txt > char_bio.txt

"""
import sys

class Processor:
    def __init__(self, raw_sent_file, mode = 'valid'):
        self.mode = mode
        self.raw_sents = {} 
        for line in raw_sent_file:
            sid, sent = line.strip().split('\t')
            self.raw_sents[sid] = sent
            
    def process(self, sid, subword_bios):
        raw_sent = self.raw_sents[sid]

        # convert subword_bios (subword list) to char_bios (syllable list)
        #         '[UNK]' to '[UNK]'
        #
        # print(subword_bios)
        char_bios = []
        for bio in subword_bios:
            subword = bio[0]
            tag = bio[1]
            if subword == '[UNK]':
                char_bios.append(('UNK', tag))
                continue
            elif subword.startswith('##'):
                subword = subword[2:]

            char_bios.append((subword[0], tag))
            if len(subword) > 1:
                if tag.startswith('B-'):
                    tag = 'I-' + tag[2:]

                for c in subword[1:]:
                    char_bios.append((c, tag))

        # 
        # print(sid, char_bios)
        print('## {}\t{}'.format(sid, raw_sent))

        i = j = 0
        while j < len(raw_sent):
            c = raw_sent[j]

            try:
                char_bios[i]
            except Exception as e:
                raise Exception('{}: char_bios[i]\n{}\ni = {}\nchar_bios = {}\nraw_sent = {}'
                                .format(e,
                                        sid,
                                        i,
                                        char_bios,
                                        raw_sent
                                        ))
            
            if char_bios[i][0] == 'UNK':
                if raw_sent[j] == ' ':
                    if char_bios[i][1].startswith('B-'):
                        self.print_bio_line('us', raw_sent[j], 'UNK', 'O', sep='\t')
                    else:
                        self.print_bio_line('us', raw_sent[j], 'UNK', char_bios[i][1], sep='\t')
                    j += 1

                is_unk_first_character = True
                while j < len(raw_sent):
                    c = raw_sent[j]

                    # change 'B-' to 'I-' if tag 
                    if is_unk_first_character:
                        self.print_bio_line('u', c, char_bios[i][0], char_bios[i][1], sep='\t')
                        is_unk_first_character = False
                    else:
                        if char_bios[i][1].startswith('B-'):
                            tag = 'I-' + char_bios[i][1][2:]
                        else:
                            tag = char_bios[i][1]
                            
                        self.print_bio_line('u', c, char_bios[i][0], tag, sep='\t')
                    
                    j += 1
                    if j >= len(raw_sent):
                        break
                    elif i == len(char_bios) - 1:
                        if j >= len(raw_sent): break
                    else:    
                        if (raw_sent[j-1] in r"′–。、"
                            or raw_sent[j] in r" ·()[]<>:;._,/!?~'-+^&"
                            or 0x4e00 <= ord(raw_sent[j]) <= 0x62ff
                            or 0x6300 <= ord(raw_sent[j]) <= 0x77ff
                            or 0x7800 <= ord(raw_sent[j]) <= 0x8cff
                            or 0x8d00 <= ord(raw_sent[j]) <= 0x9fff
                        ):
                            i += 1
                            break
            elif c == char_bios[i][0]:
                self.print_bio_line('=', c, *char_bios[i], sep='\t')
                i += 1
                j += 1
            elif c == ' ':
                if char_bios[i-1][1].startswith('B-') and char_bios[i][1].startswith('B-'):
                    tag = 'O'
                elif (char_bios[i-1][1].startswith('B-') and char_bios[i][1].startswith('I-')):
                    tag = char_bios[i][1]
                elif char_bios[i-1][1] == char_bios[i][1]:
                    tag = char_bios[i-1][1]
                else:
                    tag = 'O'
                self.print_bio_line('s', c, ' ', tag, sep='\t')
                j += 1
            else:
                self.print_bio_line('x', c, *char_bios[i], sep='\t')
                i += 1
                j += 1

       
        print('')
   
    def print_bio_line(self, check, raw_char, subword_char, bio_tag, sep = '\t'):
        if self.mode == 'valid':
            print(check, raw_char, subword_char, bio_tag, sep = sep)
        elif self.mode == 'conv':
            print(raw_char, bio_tag, sep = sep)
        else:
            raise Exception('Error: Invalid mode {}'.format(self.mod))




command = sys.argv[1]
raw_sent_filename = sys.argv[2]
subword_bio_filename = sys.argv[3]
        

raw_sent_file = open(raw_sent_filename, encoding='utf-8')
processor = Processor(raw_sent_file, mode = command)

subword_bio_file = open(subword_bio_filename, encoding='utf-8')

print(r"""## 토큰, 레이블 구분자 : \t
## 토큰 구분자 : \n
## 문장 구분자 : \n\n
## 주석 : ##
## 컬럼명 : CHAR	NE_TAG""")

for line in subword_bio_file:
    if line.startswith('## klue'):
        sid, sent = line.strip().split('\t')
        sid = sid[3:]
        bios = []
    elif line == '\n':
        processor.process(sid, bios)
        sid = None
        bios = []
    else:
        try:
            subword, tag = line.rstrip('\n').split('\t')
        except:
            print('ERROR:', line.split('\t'))
            sys.exit()

        bios.append((subword, tag))
