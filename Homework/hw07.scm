(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))


(define multiples-of-three
  (cons-stream 3 (map-stream +

(define (rle s)
  (define (helper index past lst)
    (cond
      ((null? s) (cons-stream (list past index) nil))
      ((= (car lst) past) (helper (+ index 1) past (cdr-stream lst)))
      (else (cons-stream (list past index) (helper 1 (car lst) (cdr-stream lst))))))
  (if (null? s)
        nil
        (helper (car s) 1 (cdr-stream s))
  )
)
