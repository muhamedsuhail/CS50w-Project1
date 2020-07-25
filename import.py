import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(DATABASE_URL)
db=scoped_session(sessionmaker(bind=engine))
def main():
	f=open('books.csv')
	reader=csv.reader(f)
	header=next(reader)
	for isbn,title,author,year in reader:
		db.execute("INSERT INTO books (isbn,title,author,year) VALUES(:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
		db.commit()
	f.close()
if __name__=="__main__":
	main()
