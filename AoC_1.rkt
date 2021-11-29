;;;AoC_1.rkt
;;;2021-11-28
;;;Mike Quigley
;;;I'm re-doing just day 1 part 1 of 2020 in Scheme, to prepare for 2021

#lang sicp
(define (solution? a b)
  (= 2020 (+ a b)))

;This function creates a list from an input file
(define (read-list filename)
  (define (close-file-nil file)
    (close-input-port file)
    nil)
  (define (read-list-iter file)
    (let ((line (read file)))
      (if (eof-object? line)
          (close-file-nil file)
          (cons line (read-list-iter file)))))
  (let ((file (open-input-file filename)))
    (read-list-iter file)))

(define (check-branch x l)
  (cond ((null? l) 0)
        ((solution? x (car l))
         (* x (car l)))
        (else (check-branch x (cdr l)))))

(define (check-branches l)
  (let ((result (check-branch (car l) (cdr l))))
    (if (= 0 result)
        (check-branches (cdr l))
        result)))

(define (solve1)
  (check-branches (read-list "Input1.txt")))

