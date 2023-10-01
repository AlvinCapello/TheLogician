(define (fneg p)
  (- 1 p))

(define (fcnj p q)
  (min p q))

(define (fdisj p q)
  (max p q))

(define (fcond p q)
  (max (- 1 p) q))

(define (fbic p q)
  (- 1 (abs (- p q))))

(define (fxor p q)
  (abs (- p q)))

(define (fnor p q)
  (- 1 (max p q)))

(define (fnand p q)
  (- 1 (min p q)))
