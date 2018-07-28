from datetime import datetime


def get_time_str(format="YYMMDD-HHMMSS"):
    """�ð� ���� ���ڿ��� �ش��ϴ� ���� ��¥ ���ڿ��� �����Ͽ� ��ȯ�մϴ�.

    :param format:
    :return:
    """
    if format == "YYMMDD":
        t = datetime.today().strftime("%y%m%d")
    elif format == "YYYYMMDD":
        t = datetime.today().strftime("%Y%m%d")
    elif format == "YYMMDD-HHMMSS":
        t = datetime.today().strftime("%y%m%d-%H%M%S")
    else:
        t = datetime.today().strftime("%y%m%d-%H%M%S")
    return t

def get_datetime(format="YYMMDD"):
    """�ð����� ���ڿ��κ��� datetime ��ü�� �����Ͽ� ��ȯ�մϴ�.

        need to implement..

    :param format:
    :return:
    """
    return datetime.today()