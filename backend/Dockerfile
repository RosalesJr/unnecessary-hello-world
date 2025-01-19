FROM gcc:10
WORKDIR /app
COPY . .
RUN curl -o httplib.h https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h
# Add -pthread to the g++ command to link threading support
RUN g++ -o backend main.cpp -I./ -pthread
EXPOSE 8080
CMD ["./backend"]
