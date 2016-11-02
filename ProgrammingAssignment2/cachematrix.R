## This script stores a matrix inverse if its already created otherwise it creates one

## makeCaheMatrix stores the inverse in cache
makeCacheMatrix <- function(x = matrix()) {
    m <- NULL
    set <- function(y) {
        x <<- y
        m <<- NULL
    }
    get <- function() x
    setInv <- function(solve) m <<- solve
    getInv <- function() m
    list(set = set, get = get,
         setInv = setInv,
         getInv = getInv)
}


## cacheSolve gets the cached matrix if it exists otherwise it calculates it
cacheSolve <- function(x, ...) {
     ## Return a matrix that is the inverse of 'x'
    m <- x$getInv()
    if(!is.null(m)) {
        message("getting cached data")
        return(m)
    }
    data <- x$get()
    m <- solve(data, ...)
    x$setInv(m)
    m
}

#test of the functions above
z <- matrix(c(1,2,3,4),nrow=2,ncol=2)
z1 <- makeCacheMatrix(z)
cacheSolve(z1)