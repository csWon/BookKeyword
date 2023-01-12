import Kyobo
from datetime import datetime
import logging
from Tickets import tickets
from DriverManager import driverManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main
    logger = logging.getLogger()
    #
    # # 로그의 출력 기준 설정
    logger.setLevel(logging.INFO)
    #
    # # log 출력 형식
    # # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    # # log 출력
    stream_handler = logging.StreamHandler()
    # # stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    s = datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')
    logfileName = 'log_' + s + '.log'
    # logging.basicConfig(filename='./logs/'+logfileName, level=logging.INFO)
    # logging.info('startTime : ' + s)

    # log를 파일에 출력
    file_handler = logging.FileHandler('./logs/'+logfileName)
    # # file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # driver = getTorDriver()
    _tickets = tickets()
    for ticket in _tickets.getTicket():
        s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info('timeStamp : ' + s)
        for i in range(1, 50):
            dManager = driverManager()
            driver = dManager.open_browser_c()
            try:
                keyword = ticket[1]
                page = ticket[2]
                n = ticket[3]
                title = ticket[4]

                logging.info('cycle : ' + str(i))
                logging.info(driver.title)
                logging.info(driver.current_url)

                webPageClass = ticket[0](driver)
                webPageClass.do(keyword, page, n, title)
                # webPageClass

                driver.quit()
                logging.info('------------------------------')

            except Exception as e:
                logging.info("exception!!! : ", e)
                driver.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
