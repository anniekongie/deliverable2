from django.shortcuts import render
from .models import MovieInfo


# Create your views here.


def viewMovie(request, title):
    movieObj = MovieInfo.objects.get(title=title)
    return render(request, 'movieInfo.html', {'movie':movieObj})

def movieSort(request, modelType):
    movieResults = MovieInfo.objects.filter(modelType__exact=modelType)
    return render(request, 'movieResults.html', {'movies':movieResults,'modelType':modelType})

def movieSearch(request):
    if request.method =='POST':
        query = request.POST['query']
        print(query)
        if len(query)==0:
            movieObj=MovieInfo.objects.all()
            return render(request, 'home.html', {'movies':movieObj})
        else:
            results = MovieInfo.objects.filter(title__icontains=query)
            if results:
                context={
                    'movies': results,
                    'query':query,
                    }
                return render(request, 'searchResults.html', context)
            #'movies': results
    else:
        movieObj=MovieInfo.objects.all()
        return render(request, 'home.html', {'movies': movieObj})

