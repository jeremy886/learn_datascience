## Put comments here that give an overall description of what your
## functions do


## This function creates a cached copy of a matrix to save extra costly computation

makeCacheMatrix <- function(x = matrix()) {
  s <- NULL
  
  set <- function(y) {
    x <<- y
    s <<- NULL
  }
  
  get <- function() x
  
  setsolve <- function(solve) s <<- solve
  getsolve <- function() s
  
  list(set=set, get=get, setsolve=setsolve, getsolve=getsolve)
}



## This function will find an inverse matrix of the given first parameter and save the computation
## result in a cache copy of matrix

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
    s <- x$getsolve()
    if (! is.null(s)) {
      message("getting chached data")
      return(s)
    }
    data <- x$get()
    s<-solve(data, ...)
    x$setsolve(s)
    s
}
