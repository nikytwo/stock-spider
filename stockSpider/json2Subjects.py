import json


class Subject:
    def __init__(self):
        self.date = ''
        self.name = ''
        self.value = ''


if __name__ == '__main__':

    # json to Subject class object
    with open('../finance/300115.json') as json_file:
        datas = json.load(json_file)
        finance = {}
        for k, v in datas.items():
            if ('name' == k):
                continue
            names = v['title']
            d = v['simple']
            dates = d[0]
            subjects = []
            for x in range(len(dates)):
                date = dates[x]
                for i in range(1, len(names)):
                    subject = Subject()
                    subject.date = date
                    subject.name = names[i][0]
                    subject.value = d[i][x]
                    subjects.append(subject)

            finance[k] = subjects
            print subjects

        print datas
