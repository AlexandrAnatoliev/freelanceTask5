# freelanceTask5

# Битовые операции по заданиям на python
#
# Описание
#
# программирование.
# Разработка с нуля.
# 1. С клавиатуры вводится 32-разрядное целое число a в двоичной системе счисления.
# А. Вывести k –ый бит числа a. Номер бита предварительно запросить у пользователя.
# Б. Установить/снять k –ый бит числа a.
# В. Поменять местами i –ый и j –ый биты в числе a. Числа i и j предварительно запросить у пользователя
# Г. Обнулить младшие m бит.
# 2. Дано 2^p разрядное целое число. «Поксорить» все биты этого числа друг с другом.
# 3. Написать методы циклического сдвига в 2^p разрядном целом числе на n бит влево и вправо.


# 1. С клавиатуры вводится 32-разрядное целое число a в двоичной системе счисления.
# **********************************************************************************************************************


string_number = str(input("Введите 32-разрядное число в двоичной системе счисления: "))


def str_to_int_convertion(bin_number):
    # функция для перевода строки в 10-ричное число
    bin_number = int(bin_number, 2)  # перевод строки в 10-ное число из двоичной строки
    return bin_number


binary_number = str_to_int_convertion(string_number)  # число в десятичном виде

# А. Вывести k –ый бит числа a. Номер бита предварительно запросить у пользователя.
# **********************************************************************************************************************

# Маска из 32 нулей и единицы в заданном месте
k = int(input("Введите искомый номер бита: "))


def mask_create(bit, lenght):
    # Функция для создания маски заданной длины из нулей с единицей в заданном месте. Вывод - строка
    bit_mask_list = ['0'] * lenght  # используются символы ('0' и '1') вместо чисел, т.к "join()" не работает с числами
    bit_mask_list[-(bit + 1)] = '1'  # счет битов начинается с '0'
    bit_mask_string = ", ".join(bit_mask_list).replace(", ", "")
    return bit_mask_string


bit_mask_str = mask_create(k, 32)  # маска в виде строки
binary_bit_mask = str_to_int_convertion(bit_mask_str)  # маска в формате десятичного числа


def number_mask_compare(number, mask):
    # функция сравнения вводимого числа и маски в десятичном виде
    # десятичный вид используется т.к функция 'bin' выводит данные в виде строки и битовые операции невозможны
    # если вывод - 0, то искомый бит - 0, иначе - 1
    value = 0 if number & mask == 0 else 1
    return value


bit_value = number_mask_compare(binary_number, binary_bit_mask)
print(f"{k}-й бит числа {string_number} равен {bit_value}")


# Б. Установить/снять k –ый бит числа a.
# **********************************************************************************************************************
def bit_xor(number, mask):
    # функция для изменения значения битов в числе,отмеченных '1' в маске
    number_xor = number ^ mask
    return number_xor


num_xor = bit_xor(binary_number, binary_bit_mask)


def int_to_bin_string_convertion(number):
    # функция для перевода десятичного числа в двоичное число (без '0b') в виде строки
    bin_number = bin(number)
    bin_number_string = bin_number[2:]
    return bin_number_string


num_xor_string = int_to_bin_string_convertion(num_xor)

print(f"При изменении {k}-ого бита в числе {string_number} получим число {num_xor_string}")

# В. Поменять местами i –ый и j –ый биты в числе a. Числа i и j предварительно запросить у пользователя
# **********************************************************************************************************************

i, j = map(int, input("Введите номера битов, которые необходимо поменять местами: ").split())

i_mask = mask_create(i, 32)  # Маска i - бита в виде строки нулей и еденицы
i_mask_number = str_to_int_convertion(i_mask)  # маска в виде десятичного числа
i_mask_value = number_mask_compare(binary_number, i_mask_number)  # значение i-бита заданного числа

j_mask = mask_create(j, 32)
j_mask_number = str_to_int_convertion(j_mask)
j_mask_value = number_mask_compare(binary_number, j_mask_number)

if i_mask_value != j_mask_value:
    i_j_binary_number = bit_xor(binary_number, i_mask_number)
    i_j_binary_number = bit_xor(i_j_binary_number, j_mask_number)
else:
    i_j_binary_number = binary_number

i_j_binary_string = int_to_bin_string_convertion(i_j_binary_number)

print(f"При замене битов {i} и {j} в числе {string_number} местами, искомое число будет: {i_j_binary_string}")

# Г. Обнулить младшие m бит.
# **********************************************************************************************************************
m = int(input("Введите, сколько битов нужно обнулить: "))


def bit_to_zero_mask(bits, lenght):
    # Функция для создания маски заданной длины из единиц с заданным количеством нулей. Вывод - строка
    bit_mask_list = ['1'] * lenght  # используются символы ('0' и '1') вместо чисел, т.к "join()" не работает с числами
    for i in range(bits):
        bit_mask_list[-(i + 1)] = '0'  # счет битов начинается с '0'
        bit_mask_string = ", ".join(bit_mask_list).replace(", ", "")
    return bit_mask_string


m_mask_string = bit_to_zero_mask(m, 32)  # Маска с 'm' нулями
m_mask = str_to_int_convertion(m_mask_string)  # маска в виде десятичного числа
binary_number_m_zero = binary_number & m_mask  # число с обнуленными 'm' битами в виде десятичного числа
string_number_m_zero = int_to_bin_string_convertion(binary_number_m_zero)  # в виде строки '0' и '1'

print(f"При обнулении {m} младших битов в числе {string_number} получим {string_number_m_zero}")

# 2. Дано 2^p разрядное целое число. «Поксорить» все биты этого числа друг с другом.
# **********************************************************************************************************************

string_number2 = str(input("Введите 2^p-разрядное число в двоичной системе счисления: "))
binary_number2 = str_to_int_convertion(string_number2)
string_number2_len = len(string_number2)  # сколькиразрядное число
binary_number2_xor = str_to_int_convertion(string_number2[:])  # создаю копию числа, а не ссылку на него!

for i in range(string_number2_len):
    mask_xor = mask_create(i, string_number2_len)  # маска c '1' в позиции 'i' для XOR числа
    mask_xor_number = str_to_int_convertion(mask_xor)
    binary_number2_xor = bit_xor(binary_number2_xor,
                                 mask_xor_number)  # XORим 'i' бит числа, результат - десятичное число
# добавляем '0' слева для красоты
string_number2_xor = int_to_bin_string_convertion(binary_number2_xor)
string_number2_xor = string_number2_xor.rjust(string_number2_len, '0')
print(f"Если 'поксорить' все биты числа {string_number2}, то получим {string_number2_xor}")


# 3. Написать методы циклического сдвига в 2^p разрядном целом числе на n бит влево и вправо.
# **********************************************************************************************************************

def bin_number_shift_left(number, n):
    # функция для сдвига числа на 'n'битов влево
    shift_number = number << n
    return shift_number


def bin_number_shift_right(number, n):
    # функция для сдвига числа на 'n'битов вправо
    right_number = number >> n
    return right_number


n = int(input("Введите, на сколько битов нужно сдвинуть число: "))

# число после сдвига влево
shift_number_left = bin_number_shift_left(binary_number2, n)  # в виде десятичного числа
string_shift_number_left = int_to_bin_string_convertion(shift_number_left)  # двоичного числа
string_shift_number_left = string_shift_number_left.rjust(string_number2_len, '0')  # добавили нули слева

# число после сдвига вправо
shift_number_right = bin_number_shift_right(binary_number2, n)  # в виде десятичного числа
string_shift_number_right = int_to_bin_string_convertion(shift_number_right)  # двоичного числа
string_shift_number_right = string_shift_number_right.rjust(string_number2_len, '0')  # добавили нули слева

print(f"""Число {binary_number2} примет вид:
    {string_shift_number_left} - при сдвиге на {n} бит влево
    {string_shift_number_right} - при сдвиге на {n} бит вправо
    """)
