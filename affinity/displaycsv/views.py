import os
import csv
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse


# Create your views here.

def display(request):
    filename = request.GET.get('filename')
    path = 'static\\' + str(filename) + '.csv'
    index = str(request.GET.get('index'))
    tid = str(request.GET.get('tid'))
    tweet = str(request.GET.get('tweet'))
    temp = index + tid + tweet
    print(temp)
    if request.is_ajax():
        table_header = '<table class="table" id="tbl"><thead><tr>'
        if index == tid == tweet:
            table_header += '<th scope="col">index</th>' + '<th scope="col">tweetID</th>' + '<th scope="col">tweet</th>' + '</tr></thead><tbody>'
        else:
            if index == 'true':
                table_header += '<th scope="col">index</th>'
            if tid == 'true':
                table_header += '<th scope="col">tweetID</th>'
            if tweet == 'true':
                table_header += '<th scope="col">tweet</th>'
            table_header += '</tr></thead><tbody>'

        with open(os.path.join(settings.BASE_DIR, path), 'r') as file:
            tweets = csv.reader(file, skipinitialspace=True)
            table_body = table_header + format_csv_to_table(tweets, index, tid, tweet)
        return JsonResponse({'table': table_body}, status=200)
    return render(request, "home.html")


def format_csv_to_table(tweets, index, tid, tweet):
    returnstr = ""
    for entry in tweets:
        row = '<tr>'
        if index == tid == tweet:
            row = '<th scope="row">' + entry[0] + '</th><td>' + entry[1] + '</td><td>' + entry[2] + '</td>'
        else:
            if index == 'true':
                row = '<th scope="row">' + entry[0] + '</th>'
            if tid == 'true':
                row += '<td>' + entry[1] + '</td>'
            if tweet == 'true':
                row += '<td>' + entry[2] + '</td>'
        row += '</tr>'
        returnstr += row
    returnstr += '</tbody></table>'
    return returnstr
