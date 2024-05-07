def is_leap_year(year):
    """
    fungsi untuk menentukan apakah suatu tahun adalah tahun kabisat atau bukan.

    parameter:
    year (int): tahun yang ingin diperiksa.

    returns:
    bool: true jika tahun tersebut adalah tahun kabisat, false jika bukan.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# contoh penggunaan program
if __name__ == "__main__":
    year = int (input("masukan tahun: "))
    if is_leap_year(year):
        print(f"tahun {year} adalah tahun kabisat.")
    else:
        print(f"tahun{year}bukan tahun kabisat.")