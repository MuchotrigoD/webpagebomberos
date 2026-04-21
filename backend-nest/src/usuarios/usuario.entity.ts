import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from 'typeorm';

@Entity()
export class Usuario {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ length: 100 })
  nombre: string;

  @Column({ length: 100 })
  apellido: string;

  @Column({ unique: true })
  email: string;

  @Column({ length: 100 })
  password: string;

  @Column({ length: 20, nullable: true })
  dni: string;

  @Column({ length: 50, nullable: true })
  grado: string;

  @Column({ type: 'text', nullable: true })
  descripcion: string;

  @Column({ type: 'date', nullable: true })
  fecha_ingreso: string;

  @CreateDateColumn()
  creado_en: Date;
}
