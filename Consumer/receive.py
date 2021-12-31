import pika, sys, os
from NewsModel import News, engine
import json
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

def main():
    #db
    try:
        db_conn = engine.connect()
    except:
        print('DB_connection_error')

    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='POST_NEWS')

    def callback(ch, method, properties, body):
        if body:
            scanned_text = body.decode('utf-8',errors='replace')
            data = json.loads(scanned_text)
            ins = News.insert().values(data)
            try:
                rs = db_conn.execute(ins)
            except IntegrityError:
                print('news already exists')

        


    channel.basic_consume(queue='POST_NEWS', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)