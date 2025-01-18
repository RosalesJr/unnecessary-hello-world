FROM gcc:10
WORKDIR /app
COPY . .
RUN g++ -o backend main.cpp
EXPOSE 8080
CMD ["./backend"]
