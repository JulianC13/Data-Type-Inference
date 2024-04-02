from django.shortcuts import render
from django.contrib.auth.models import User
from .utils import Utils
from .serializers import DataSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
import pandas as pd
from .models import Data


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({'error': 'File not found'}, status=400)
        try:
            file = request.data['file']
            df = pd.read_csv(file)
            # print(df.dtypes)
            # Perform data processing and validation
            df = Utils.infer_and_convert_data_types(df)
            print("\nData types after inference:")
            print(df.dtypes)
            # print(len(df))
            # processed_data = df.head().to_dict(orient='records')
            processed_data = df.to_dict(orient='records')
            types = df.dtypes.apply(lambda x: x.name).to_dict()
            # print(len(processed_data))

            # Return appropriate response
            return Response({'data': processed_data,'types': types})
        except ParseError as pe:
            print(pe)
            return Response({'error': str(pe)}, status=400)
        except pd.errors.ParserError:
            return Response({'error': 'Invalid CSV format'}, status=400)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=500)
        
    
   
