# -*- coding: utf-8 -*-

# if __name__ == "__main__":
#     print "press any key"
#     input_test_word = raw_input(">>>  ")
#     print "key: " + str(input_test_word)

end_flg = True

while(end_flg):

    print "press any key (9:end)"
    input_test_word = raw_input(">>>  ")
    print "key: " + str(input_test_word)
    if int(input_test_word) == 9:
        print "end"
        end_flg = False
