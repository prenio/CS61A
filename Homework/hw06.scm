;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (unique s)
  (if (null? s) '()
    (cons (car s) (unique (filter (lambda (f) (not(equal? f (car s)))) (cdr s)))))
)

(define (cons-all first rests)
  (cond
    ((null? rests) nil)
    (else (cons(cons first (car rests))(cons-all first (cdr rests))))
    )
  )

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((null? denoms) nil)
    ((= 0 total) '(()))
    ((< total (car denoms)) (list-change total (cdr denoms)))
    (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
  )
)
; Tail recursion

(define (replicate x n)
  (define (loop y m acc)
    (if (= m 0)
      acc
      (loop y (- m 1) (append `(,y) acc))))
  (loop x n `()))


(define (accumulate combiner start n term)
    (if (= n 0) start
      (accumulate combiner (combiner (term n) start) (- n 1) term)))

(define (accumulate-tail combiner start n term)
    (if (= n 0) start
      (accumulate-tail combiner (combiner (term n) start) (- n 1) term)))

; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) , lst))

)
