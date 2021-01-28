#include <iostream>
#include "pointArray.h"

PointArray::PointArray() {
    size = 0;
    data = new Point[0]; // Porque en el destructor se delete
}

PointArray::PointArray(const Point arr[], const int size) {
    this->size = size;
    data = new Point[size];
    for(int i = 0; i < size; i++) {
        data[i] = arr[i];
    }
}

PointArray::PointArray(const PointArray &o) {
    this->size = o.size;
    data = new Point[o.size];
    for(int i = 0; i < size; i++) {
        data[i] = o.data[i];
    }
}

PointArray::~PointArray() {
    delete[] data;
}


int PointArray::getSize() const {
    return size;
}

void PointArray::push_back(const Point &p) {
    Point *tmp = new Point[size+1];
    size++;
    for(int i = 0; i < size-1; i++) {
        tmp[i] = data[i]; 
    }
    tmp[size-1] = p;
    delete[] data;
    data = tmp;
}

void PointArray::insert(const int pos, const Point &p){

	if ((pos < size )&&(-1 < pos))
		data[pos] = p;
	else 
		std::cout << "out of range" << std::endl;
	
}
void PointArray::remove(const int pos){
	Point *tmp = new Point[size];
	std::cout<<size<< std::endl;
	int j = 0;
	for (int i=0 ; i < size-1; i++){
		if (i == pos){
			tmp[i] = data[i+1];
			i++;
		}
		if (i != pos){
			tmp[j] = data[i];
		}
		j++; 
	}
	delete[] data;
	data = tmp;
	size--;
}

void PointArray::print() const {
    std::cout << "[ ";
    for(int i = 0; i < size; i++) {
        data[i].print();
        std::cout << " ";
    }
    std::cout << "]" << std::endl;
}