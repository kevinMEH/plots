all: build/$(file)
	./build/$(file)

build/$(file): $(file).c src/*.c
	gcc $(file).c library/*.c -O3 -o build/$(file)

clean:
	rm build/*