
def main():
  user-text = input("enter a sql injection hack")
  bad-query = f"SELECT dummy from dual where dummy = {user-text}"
  ...


if __name__ == "__main__":
  main()
